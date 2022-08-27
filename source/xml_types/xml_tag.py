from enum import Enum


class XMLTagTypes(Enum):
    MODEL = 'uml:Model'
    REQUIREMENT = 'Requirements:Requirement'
    REQUIREMENTS_REFINE = 'Requirements:Refine'
    REQUIREMENTS_SATISFY = 'Requirements:Satisfy'
    REQUIREMENTS_VERIFY = 'Requirements:Verify'
    BLOCK = 'Blocks:Block'
    BLOCKS_VALUE_TYPE = 'Blocks:ValueType'
    CONSTRAINT_BLOCK = 'ConstraintBlocks:ConstraintBlock'
    FLOW_PORT = 'DeprecatedElements:FlowPort'
    BLOCKS_BINDING_CONNECTOR = 'Blocks:BindingConnector'
    BLOCKS_NESTED_CONNECTOR_END = 'Blocks:NestedConnectorEnd'

    PACKAGE_IMPORT = 'packageImport'
    IMPORTED_PACKAGE = 'importedPackage'
    PACKAGED_ELEMENT = 'packagedElement'
    PROFILE_APPLICATION = 'profileApplication'
    E_ANNOTATIONS = 'eAnnotations'
    APPLIED_PROFILE = 'appliedProfile'
    REFERENCES = 'references'
    LIFELINE = 'lifeline'
    FRAGMENT = 'fragment'
    MESSAGE = 'message'
    OPERAND = 'operand'
    GUARD = 'guard'
    SPECIFICATION = 'specification'
    LANGUAGE = 'language'
    BODY = 'body'
    OWNED_BEHAVIOR = 'ownedBehavior'
    OWNED_LITERAL = 'ownedLiteral'
    OWNED_ATTRIBUTE = 'ownedAttribute'
    OWNED_CONNECTOR = 'ownedConnector'
    CHANGE_EXPRESSION = 'changeExpression'
    NESTED_CLASSIFIER = 'nestedClassifier'
    OWNED_END = 'ownedEnd'
    OWNED_RULE = 'ownedRule'
    EDGE = 'edge'
    NODE = 'node'
    REGION = 'region'
    DETAILS = 'details'
    INCLUDE = 'include'
    TYPE = 'type'
    TRANSITION = 'transition'
    SUBVERTEX = 'subvertex'
    DO_ACTIVITY = 'doActivity'
    ENTRY = 'entry'
    END = 'end'
    TRIGGER = 'trigger'
    DEFAULT_VALUE = 'defaultValue'