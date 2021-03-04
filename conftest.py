import pytest
import os


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    if os.environ.get("REGRESSION_MODE") == "off":
        yield
        return
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        properties = {}
        for k, v in report.user_properties:
            properties[k] = v
        img = "file://{}/{}.png".format(properties["output"], properties["test_name"])

        if properties.get("new-test", True):
            extra.append(pytest_html.extras.html("<table>"))
            extra.append(pytest_html.extras.html("<tr><th colspan='2'> Directory : {}   Python script : {}.py </th></tr>".format(properties["directory"], properties["test_name"])))
            extra.append(
                pytest_html.extras.html(
                    "<tr><th colspan='2'>new test : {} </th></tr>".format(
                        properties["test_name"]
                    )
                )
            )
            extra.append(pytest_html.extras.html("<tr>"))
            extra.append(
                pytest_html.extras.html(
                    "<td> <img src='{}' width='50%'/></td>".format(img)
                )
            )
            extra.append(pytest_html.extras.html("<tr>"))
            extra.append(pytest_html.extras.html("</table>"))

        else:
            diff = "file://{}".format(properties["diff-image"])
            ref = "file://{}".format(properties["ref-image"])
            extra.append(pytest_html.extras.html("<table>"))
            extra.append(pytest_html.extras.html("<tr><th colspan='4'> Directory : {}   Python script : {}.py </th></tr>".format(properties["directory"], properties["test_name"])))
            extra.append(
                pytest_html.extras.html(
                    "<tr><th colspan='2'>Difference in pixels : {} Test : {} </th></tr>".format(
                        properties.get("diff", "undef"), properties["test_name"]
                    )
                )
            )
            extra.append(pytest_html.extras.html("<tr>"))
            extra.append(
                pytest_html.extras.html(
                    "<td> <img src='{}' width='50%'/></td>".format(ref)
                )
            )
            extra.append(
                pytest_html.extras.html(
                    "<td> <img src='{}'  width='50%'/></td>".format(diff)
                )
            )
            extra.append(
                pytest_html.extras.html(
                    "<td> <img src='{}'  width='50%'/></td>".format(img)
                )
            )
            extra.append(pytest_html.extras.html("<tr>"))
            extra.append(pytest_html.extras.html("</table>"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extra.append(pytest_html.extras.html("<div>Additional HTML</div>"))
        report.extra = extra
