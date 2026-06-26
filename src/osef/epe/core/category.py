from enum import Enum

class Category(str, Enum):
    ARCHITECTURE = "Architecture"
    DOCUMENTATION = "Documentation"
    DEPENDENCIES = "Dependencies"
    CONFIGURATION = "Configuration"
    COMPLEXITY = "Complexity"
    MAINTAINABILITY = "Maintainability"
    SECURITY = "Security"
    TESTING = "Testing"
    PLUGINS = "Plugins"
    PERFORMANCE = "Performance"
    NAMING = "Naming"
    STYLE = "Style"
    REPOSITORY_HEALTH = "Repository Health"
