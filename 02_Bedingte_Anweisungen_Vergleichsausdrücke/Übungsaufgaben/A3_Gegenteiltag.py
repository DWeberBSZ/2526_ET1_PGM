"""
- Analysieren Sie den nachfolgenden Programmcode und beschreiben Sie ihn mit aussagekräftigen Kommentaren.

Zeit: 5 Minuten, Einzelarbeit
"""
today_is_opposite_day = True

if today_is_opposite_day == True:
    say_it_is_opposite_day = True
else:
    say_it_is_opposite_day = False

if today_is_opposite_day == True:
    say_it_is_opposite_day = not say_it_is_opposite_day

if say_it_is_opposite_day == True:
    print('Heute ist Gegenteil-Tag.')
else:
    print('Heute ist nicht Gegenteil-Tag.')