# Enumerific Enumerations Library Change Log

## [1.0.5] - 2025-08-01
### Added
- Added default initialisation of the annotations (`anno`) class instance, including for
enumeration options that were specified without the `anno` class, for consistency with
enumeration options that were specified with the `anno` class.
- Added access to an enumeration option's annotations (`anno`) class instance via the new `annotations` property.

## [1.0.4] - 2025-06-29
### Added
- Improved attribute access on reconciled enumeration options for class methods, instance methods and properties.

## [1.0.3] - 2025-06-28
### Added
- Support for accessing attributes (methods, properties, etc) of a subclassed enumeration.
- Support for controlling whether enumeration options added to a subclass are backfilled on the superclass.
- Support for controlling whether enumeration classes can be extended through subclassing and registration.

## [1.0.2] - 2025-06-22
### Added
- Support for annotating an enumeration option with other properties in addition to its value.
- Added unit tests for annotations (`anno`), automatically generating number sequences
(`auto`) and enumeration membership in native container types (`list`, `set`, `tuple`).

## [1.0.1] - 2025-06-05
### Added
- Support for extensible enumerations via the new `Enumeration` class and subclasses.

## [1.0.0] - 2025-01-21
### Added
- First release of the Enumerific enumerations library.