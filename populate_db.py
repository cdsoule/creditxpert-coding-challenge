from challenge1.models import Shape, ColorScheme

def populate_shapes():
    shapes = (
        ('circle', 'fa-solid fa-circle'),
        ('square', 'fa-solid fa-square'),
        ('cowboy hat', 'fa-solid fa-hat-cowboy'),
        ('star', 'fa-solid fa-star')
    )

    for name, fa_class in shapes:
        Shape.objects.create(name=name, fa_class=fa_class)

def populate_colors():
    colors = (
        ('#124076', '#7F9F80', '#F9E897', '#FFC374'),
        ('#5E1675', '#EE4266', '#FFD23F', '#337357'),
        ('#D04848', '#F3B95F', '#FDE767', '#6895D2'),
        ('#D3D3D3', '#A9A9A9', '#696969', '#202020')
    )

    for color1, color2, color3, color4 in colors:
        ColorScheme.objects.create(color1=color1, color2=color2, color3=color3, color4=color4)

if __name__ == '__main__':
    populate_shapes()
    populate_colors()