from builders import AbstractBuilder

class EnvDirector:

    @staticmethod
    def create_full_env(builder: AbstractBuilder):
        builder.deploy_os_image()
        builder.create_virtual_environment()
        builder.install_dependencies()
        builder.install_app()
        return builder.get_env()

    @staticmethod
    def create_env_without_app(builder: AbstractBuilder):
        builder.deploy_os_image()
        builder.create_virtual_environment()
        builder.install_dependencies()
        return builder.get_env()
