from styles import Style

class Residence:

    def __init__(self, address, style):
        self.address = address
        self.style = style
    
    @classmethod
    def validate_style(cls, address, style):
        if Style.is_valid_style(style):
            return cls(address, Style(style))
        else:
            raise Exception('"{}" is not a valid style. If it should be, consider adding it to the style file located. {}'.format(style, Style.data_path()))

    
r1 = Residence.validate_style('202 Main St.','Detahed')
r2 = Residence.validate_style('201 Main St.','Detached')