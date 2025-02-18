from prompt_toolkit.validation import Validator, ValidationError

class NoneValidator(Validator):
    def validate(self, document):
        return

class IntValidator(Validator):
    def validate(self, document):
        if document.text == '':
            return 0
        try:
            return int(document.text)
        except ValueError:
            raise ValidationError(
                message='Please enter a number',
                cursor_position=len(document.text))

class NotNull(Validator):
    def validate(self, document):
        if document.text == '':
            raise ValidationError(
                message="Please enter a string",
                cursor_position=len(document.text))