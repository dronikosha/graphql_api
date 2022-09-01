from environs import Env

env = Env()
env.read_env()

key = env('SECRET_KEY')