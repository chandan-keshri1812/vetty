import os

class Config:
    COINGECKO_API_KEY = os.getenv('COINGECKO_API_KEY', 'CG-C9d8UGLiQ4um9G4wANdjhPhJ')
    API_KEY = os.getenv('API_KEY', 'supersecretkey') 