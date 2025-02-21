""" =================================================
Copyright (C) 2018 Vikash Kumar
Author  :: Vikash Kumar (vikashplus@gmail.com)
Source  :: https://github.com/vikashplus/robohive
License :: Under Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
================================================= """


# RoboHive version
__version__ = "0.6.0"


# Check for RoboHive initialization
from robohive.utils.import_utils import simhive_isavailable
simhive_isavailable(robohive_version = __version__)


# Register RoboHive Envs
import gym
_current_gym_envs = gym.envs.registration.registry.env_specs.keys()
_current_gym_envs = set(_current_gym_envs)
robohive_env_suite = set()

# Register Arms Suite
import robohive.envs.arms # noqa
robohive_arm_suite = set(gym.envs.registration.registry.env_specs.keys())-robohive_env_suite-_current_gym_envs
robohive_arm_suite = set(sorted(robohive_arm_suite))
robohive_env_suite = robohive_env_suite | robohive_arm_suite

# All RoboHive Envs
robohive_env_suite = sorted(robohive_env_suite)