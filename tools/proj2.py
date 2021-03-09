import json
import jinja2


with open("../magics-bitbucket/share/magics/epsg.json", "r") as f:
    data = json.load(f)

with open("projfull.template", "r") as source:
    template = jinja2.Template(source.read())


for i in data["definitions"]:
    for epsg in i:
        print(epsg)
        py = "proj-regression-{}.py".format(epsg)
        py = py.replace(":", "-")
        with open(py, "wt") as out:
            out.write(template.render(epsg=epsg,))
