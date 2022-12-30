from builders import TestingBuilder, StagingBuilder

from director import EnvDirector
from environment import Environment

default_testing_environment = Environment('Testing env')
testing_builder = TestingBuilder(default_testing_environment)
full_testing_env = EnvDirector.create_full_env(testing_builder)
print()
print(full_testing_env)

print()
testing_env_without_app = EnvDirector.create_env_without_app(testing_builder)
print()
print(testing_env_without_app)

default_staging_environment = Environment('Staging env')
staging_builder = StagingBuilder(default_staging_environment)

full_staging_env = EnvDirector.create_full_env(staging_builder)
print()
print(full_staging_env)

print()
staging_env_without_app = EnvDirector.create_env_without_app(staging_builder)
print()
print(staging_env_without_app)