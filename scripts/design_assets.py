"""Build the profile's original, self-contained SVG artwork (stdlib only)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / 'assets'
PALETTES = {
    'light': dict(bg='#E6EFF4', ink='#17384A', muted='#486271', line='#B4CDD8', paper='#F9FCFC', coral='#C44832', peach='#F3CFB9', green='#C7DCD2', blue='#B6CEE5'),
    'dark': dict(bg='#173442', ink='#EDF5F3', muted='#B6CDD5', line='#456574', paper='#244958', coral='#FFAB8F', peach='#765647', green='#3B675C', blue='#385D7A'),
}


def svg(body, p, height, title, description, width=960):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{title}</title><desc id="desc">{description}</desc>
<style>text{{font-family:'Avenir Next',Avenir,'Trebuchet MS',Arial,sans-serif;fill:{p['ink']}}}.small{{font-size:16px;letter-spacing:2px;font-weight:600}}.muted{{fill:{p['muted']}}}.line{{stroke:{p['ink']};stroke-width:3;fill:none;stroke-linecap:round;stroke-linejoin:round}}</style>
{body}
</svg>\n'''


def hero(p):
    body = f'''<rect width="960" height="358" rx="20" fill="{p['bg']}"/>
<!-- A continuous observation line joins a photo, a city walk and a saved task. -->
<path d="M526 291 C558 302 558 239 612 240 S697 285 729 232 S798 143 858 177 S896 292 855 313" stroke="{p['coral']}" stroke-width="3" fill="none" stroke-linecap="round"/>
<circle cx="526" cy="291" r="6" fill="{p['coral']}"/><circle cx="855" cy="313" r="6" fill="{p['coral']}"/>
<text x="42" y="46" class="small">YUQIN WANG</text>
<text x="42" y="131" font-size="70" font-weight="750" letter-spacing="-3">Small apps.</text>
<text x="42" y="209" font-size="76" font-family="Georgia,serif" font-style="italic" letter-spacing="-3" style="font-family:Georgia,serif">Real life.</text>
<path d="M45 229 Q206 241 357 227" fill="none" stroke="{p['coral']}" stroke-width="5" stroke-linecap="round"/>
<text x="43" y="281" font-size="21" class="muted">Everyday curiosity. Useful AI tools.</text>
<text x="43" y="322" class="small muted">INDEPENDENT MAKER  /  yuqin.wang</text>
<!-- Photo observation: viewfinder corners, a leaf, and a source label. -->
<g transform="translate(555 58) rotate(-8 70 86)">
<rect x="5" y="7" width="145" height="178" rx="6" fill="{p['line']}"/>
<rect width="145" height="178" rx="6" fill="{p['paper']}" stroke="{p['line']}"/>
<rect x="14" y="14" width="117" height="113" rx="3" fill="{p['green']}"/>
<path d="M26 38 V27 H38 M107 27 H119 V38 M26 103 V115 H38 M107 115 H119 V103" class="line" opacity=".6"/>
<path d="M57 100 Q61 67 92 42 Q110 80 69 90 M61 90 L88 53" class="line"/>
<circle cx="22" cy="147" r="4" fill="{p['coral']}"/>
<path d="M35 147 H115 M18 160 H83" stroke="{p['line']}" stroke-width="4" stroke-linecap="round"/>
</g>
<!-- City walk: a folded map and one chosen route. -->
<g transform="translate(732 41) rotate(9 80 70)">
<path d="M0 12 L53 0 L108 13 L158 1 V144 L108 156 L53 143 L0 155 Z" fill="{p['paper']}" stroke="{p['line']}" stroke-width="2"/>
<path d="M53 0 V143 M108 13 V156 M0 58 L53 46 L108 59 L158 47 M0 108 L53 96 L108 109 L158 97" fill="none" stroke="{p['line']}" stroke-width="2"/>
<path d="M26 129 L26 80 L83 92 L83 41 L132 30" stroke="{p['coral']}" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="26" cy="129" r="6" fill="{p['coral']}"/>
<circle cx="132" cy="30" r="9" fill="{p['peach']}" stroke="{p['coral']}" stroke-width="3"/>
</g>
<!-- Continuity: a bookmark carried to the next task. -->
<g transform="translate(715 237) rotate(-5 75 43)">
<rect width="149" height="72" rx="12" fill="{p['blue']}"/>
<path d="M22 0 V42 L34 33 L46 42 V0" fill="{p['coral']}"/>
<path d="M67 26 H121 M67 39 H103 M113 48 L121 40 L129 48 M121 40 V58" class="line"/>
</g>
<path d="M902 312 H919 M910.5 303.5 V320.5" class="line" opacity=".65"/>
'''
    return svg(body, p, 358, 'Yuqin Wang — Small apps. Real life.', 'Original illustration: a photo observation card, a folded city map, and a task bookmark connected by one line. Apps for everyday life and tools for working with AI.')


def continuity(p):
    body = f'''<rect width="960" height="168" rx="16" fill="{p['bg']}"/>
<path d="M300 83 H345 M330 70 L345 83 L330 96 M620 83 H665 M650 70 L665 83 L650 96" class="line"/>
<g transform="translate(29 30)"><rect width="248" height="108" rx="12" fill="{p['paper']}"/>
<circle cx="23" cy="24" r="5" fill="{p['coral']}"/>
<text x="43" y="32" font-size="24" font-weight="650">Decisions</text><text x="23" y="75" font-size="24" class="muted">+ evidence</text></g>
<g transform="translate(362 30)"><rect width="241" height="108" rx="12" fill="{p['blue']}"/>
<path d="M21 0 V36 L31 28 L41 36 V0" fill="{p['coral']}"/>
<text x="59" y="35" font-size="24" font-weight="650">Checkpoint</text><text x="23" y="78" font-size="23">Save the next step</text></g>
<g transform="translate(685 30)"><rect width="246" height="108" rx="12" fill="{p['green']}"/>
<text x="23" y="36" font-size="24" font-weight="650">Next session</text><text x="23" y="78" font-size="24">Pick up here ↗</text></g>'''
    return svg(body, p, 168, 'Context Continuity workflow', 'Decisions and evidence become a checkpoint containing the next step, so the next session can resume the task. This is a workflow illustration, not a terminal screenshot.')


def continuity_mobile(p):
    body = f'''<rect width="440" height="366" rx="16" fill="{p['bg']}"/>
<path d="M219 102 V131 M210 122 L219 131 L228 122 M219 232 V261 M210 252 L219 261 L228 252" class="line"/>
<rect x="22" y="20" width="396" height="80" rx="12" fill="{p['paper']}"/>
<circle cx="48" cy="59" r="5" fill="{p['coral']}"/>
<text x="69" y="67" font-size="27" font-weight="650">Decisions + evidence</text>
<rect x="22" y="134" width="396" height="96" rx="12" fill="{p['blue']}"/>
<path d="M45 134 V173 L55 165 L65 173 V134" fill="{p['coral']}"/>
<text x="84" y="173" font-size="27" font-weight="650">Checkpoint</text><text x="45" y="210" font-size="25">Save the next step</text>
<rect x="22" y="264" width="396" height="80" rx="12" fill="{p['green']}"/>
<text x="45" y="313" font-size="27" font-weight="650">Next session: resume ↗</text>'''
    return svg(body, p, 366, 'Context Continuity workflow', 'Decisions and evidence become a checkpoint with the next step. Resume from it in the next session.', width=440)


if __name__ == '__main__':
    for theme, palette in PALETTES.items():
        for name, build in [('maker', hero), ('continuity', continuity), ('continuity-mobile', continuity_mobile)]:
            (ROOT / f'{name}-{theme}.svg').write_text(build(palette))
