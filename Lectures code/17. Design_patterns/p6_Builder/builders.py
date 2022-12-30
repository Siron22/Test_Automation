from abc import ABC, abstractmethod
import copy


class AbstractBuilder(ABC):

    @abstractmethod
    def deploy_os_image(self):
        pass

    @abstractmethod
    def create_virtual_environment(self):
        pass

    @abstractmethod
    def install_dependencies(self):
        pass

    @abstractmethod
    def install_app(self):
        pass

    @abstractmethod
    def get_env(self):
        pass


class TestingBuilder(AbstractBuilder):

    def __init__(self, environment):
        self.environment = environment

    def deploy_os_image(self):
        print("Deploy OS on testing env")
        self.environment.update_env_stage("Deploy OS on testing env")

    def create_virtual_environment(self):
        print("Create venv on testing env")
        self.environment.update_env_stage("Create venv on testing env")

    def install_dependencies(self):
        print("Installing dependencies on testing env")
        self.environment.update_env_stage("Installing dependencies on testing env")

    def install_app(self):
        print("Installing app on testing env")
        self.environment.update_env_stage("Installing app on testing env")

    def reset(self):
        self.environment.clear()

    def get_env(self):
        result = copy.deepcopy(self.environment)
        self.reset()
        return result


class StagingBuilder(AbstractBuilder):

    def __init__(self, environment):
        self.environment = environment

    def deploy_os_image(self):
        print("Deploy OS on staging env")
        self.environment.update_env_stage("Deploy OS on staging env")

    def create_virtual_environment(self):
        print("Create venv on staging env")
        self.environment.update_env_stage("Create venv on staging env")

    def install_dependencies(self):
        print("Installing dependencies on staging env")
        self.environment.update_env_stage("Installing dependencies on staging env")

    def install_app(self):
        print("Installing app on staging env")
        self.environment.update_env_stage("Installing app on staging env")

    def reset(self):
        self.environment.clear()

    def get_env(self):
        result = copy.deepcopy(self.environment)
        self.reset()
        return result