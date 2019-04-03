#!/usr/bin/env python
from gym.envs.registration import register
from gym import envs


def RegisterOpenAI_Ros_Env(task_env, timestep_limit_per_episode=10000):
    """
    Registers all the ENVS supported in OpenAI ROS. This way we can load them
    with variable limits.
    Here is where you have to PLACE YOUR NEW TASK ENV, to be registered and accesible.
    return: False if the Task_Env wasnt registered, True if it was.
    """

    ###########################################################################
    # MovingCube Task-Robot Envs

    result = True

    # Cubli Moving Cube
    if task_env == 'MovingCubeOneDiskWalk-v0':
        # We register the Class through the Gym system
        register(
            id=task_env,
            entry_point='openai_ros:task_envs.moving_cube.one_disk_walk.MovingCubeOneDiskWalkEnv',
            timestep_limit=timestep_limit_per_episode,
        )
        # We have to import the Class that we registered so that it can be found afterwards in the Make
        from openai_ros.task_envs.moving_cube import one_disk_walk

    # Husarion Robot
    elif task_env == 'HusarionGetToPosTurtleBotPlayGround-v0':

        register(
            id=task_env,
            entry_point='openai_ros:task_envs.husarion.husarion_get_to_position_turtlebot_playground.HusarionGetToPosTurtleBotPlayGroundEnv',
            timestep_limit=timestep_limit_per_episode,
        )

        # import our training environment
        from openai_ros.task_envs.husarion import husarion_get_to_position_turtlebot_playground

    elif task_env == 'FetchTest-v0':
        register(
            id=task_env,
            entry_point='openai_ros:task_envs.fetch.fetch_test_task.FetchTestEnv',
            timestep_limit=timestep_limit_per_episode,
        )
        # 50
        # We have to import the Class that we registered so that it can be found afterwards in the Make
        from openai_ros.task_envs.fetch import fetch_test_task

    elif task_env == 'CartPoleStayUp-v0':

        register(
            id=task_env,
            entry_point='openai_ros:task_envs.cartpole_stay_up.stay_up.CartPoleStayUpEnv',
            timestep_limit=timestep_limit_per_episode,
        )

        # import our training environment
        from openai_ros.task_envs.cartpole_stay_up import stay_up

    elif task_env == 'HopperStayUp-v0':

        register(
            id=task_env,
            entry_point='openai_ros:task_envs.hopper.hopper_stay_up.HopperStayUpEnv',
            timestep_limit=timestep_limit_per_episode,
        )

        # import our training environment
        from openai_ros.task_envs.hopper import hopper_stay_up

    # Add here your Task Envs to be registered
    else:
        result = False

    ###########################################################################

    if result:
        # We check that it was really registered
        supported_gym_envs = GetAllRegisteredGymEnvs()
        #print("REGISTERED GYM ENVS===>"+str(supported_gym_envs))
        assert (task_env in supported_gym_envs), "The Task_Robot_ENV given is not Registered ==>" + \
            str(task_env)

    return result


def GetAllRegisteredGymEnvs():
    """
    Returns a List of all the registered Envs in the system
    return EX: ['Copy-v0', 'RepeatCopy-v0', 'ReversedAddition-v0', ... ]
    """

    all_envs = envs.registry.all()
    env_ids = [env_spec.id for env_spec in all_envs]

    return env_ids