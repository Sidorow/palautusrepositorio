from urllib import request
from project import Project
import tomli


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        #tiedoston merkkijonomuotoinen sisalto
        content = request.urlopen(self._url).read().decode("utf-8")
        toml_content = tomli.loads(content)
        #print(toml_content["tool"]["poetry"]["dependencies"])
        dependencies = toml_content["tool"]["poetry"]["dependencies"]
        dev_dependencies = toml_content["tool"]["poetry"]["dev-dependencies"]

        #deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project("Test name", "Test description", dependencies, dev_dependencies)
