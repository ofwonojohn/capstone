from flask import Flask
from flask_cors import CORS
from config import config
from database import init_db

# Import all route blueprints
from routes.programs import programs_bp
from routes.facilities import facilities_bp
from routes.services import services_bp
from routes.equipment import equipment_bp
from routes.projects import projects_bp
from routes.participants import participants_bp
from routes.outcomes import outcomes_bp
# from routes.project_participants import project_participants_bp

def create_app(config_name='development'):
    """Application factory function"""
    
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    CORS(app)
    db = init_db(app)
    
    # Create upload directory if it doesn't exist
    import os
    upload_dir = app.config['UPLOAD_FOLDER']
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
        os.makedirs(os.path.join(upload_dir, 'outcomes'))
    
    # Register all blueprints with API prefix
    app.register_blueprint(programs_bp, url_prefix='/api/programs')
    app.register_blueprint(facilities_bp, url_prefix='/api/facilities')
    app.register_blueprint(services_bp, url_prefix='/api/services')
    app.register_blueprint(equipment_bp, url_prefix='/api/equipment')
    app.register_blueprint(projects_bp, url_prefix='/api/projects')
    app.register_blueprint(participants_bp, url_prefix='/api/participants')
    app.register_blueprint(outcomes_bp, url_prefix='/api/outcomes')
    # app.register_blueprint(project_participants_bp, url_prefix='/api/project-participants')
    
    # Basic health check endpoint
    @app.route('/health')
    def health_check():
        return {'status': 'healthy', 'service': 'AP Capstone API'}, 200
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return {'error': 'Resource not found'}, 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return {'error': 'Internal server error'}, 500
    
    return app

# For running directly
if __name__ == '__main__':
    app = create_app('development')
    app.run(debug=True, host='0.0.0.0', port=5000)