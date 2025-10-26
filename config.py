# import os
# from dotenv import load_dotenv

# # Cargar variables de entorno desde .env
# load_dotenv()

# class Config:
#     """Configuración base"""
#     SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-change-in-production')
#     JWT_EXPIRATION_HOURS = int(os.getenv('JWT_EXPIRATION_HOURS', 24))
#     DEBUG = False
#     DATA_DIR = os.getenv('DATA_DIR', './data')

# class DevelopmentConfig(Config):
#     """Configuración de desarrollo"""
#     DEBUG = True
#     TESTING = False
#     ENV = 'development'

# class ProductionConfig(Config):
#     """Configuración de producción"""
#     DEBUG = False
#     TESTING = False
#     ENV = 'production'

# class TestingConfig(Config):
#     """Configuración de testing"""
#     DEBUG = True
#     TESTING = True
#     ENV = 'testing'

# config = {
#     'development': DevelopmentConfig,
#     'production': ProductionConfig,
#     'testing': TestingConfig,
#     'default': DevelopmentConfig
# }