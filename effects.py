from pygame import draw, transform, image
from settings import BLACK

C_IMG = transform.scale(image.load('assets/images/notes/c.png').convert_alpha(), (50, 50))
D_IMG = transform.scale(image.load('assets/images/notes/d.png').convert_alpha(), (50, 50))
E_IMG = transform.scale(image.load('assets/images/notes/e.png').convert_alpha(), (50, 50))

NOTE_IMAGES = {
    'C': C_IMG,
    'D': D_IMG,
    'E': E_IMG,
}

_FLYING_NOTES = []

def spawn_flying_note(rect, note_name: str | None):
    if not note_name:
        return
    img = NOTE_IMAGES.get(note_name)
    if not img:
        return
    x = rect.centerx - img.get_width() // 2
    y = rect.y - img.get_height() - 10
    _FLYING_NOTES.append({'img': img, 'x': x, 'y': y, 'vy': -1})


def update_and_draw_flying_notes(screen):
    to_remove = []
    for n in _FLYING_NOTES:
        n['y'] += n['vy']
        screen.blit(n['img'], (n['x'], n['y']))
        if n['y'] + n['img'].get_height() < 0:
            to_remove.append(n)

    for n in to_remove:
        _FLYING_NOTES.remove(n)


def draw_key_effect(screen, rect, is_pressed=False, note=None):
    if not is_pressed:
        base_color = (220, 223, 228)
    else:
        base_color = (170, 223, 255)

    draw.rect(screen, base_color, rect, border_radius=3)
    draw.rect(screen, BLACK, rect, 2, border_radius=1)
