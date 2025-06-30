# -*- coding: utf-8 -*-

print("🏁 لعبة السباق الثلاثي 🏁")
print("يتنافس فيها لاعبان في ثلاث رياضات:\n1- السباحة 🏊‍♂️\n2- ركوب الدراجة 🚴\n3- الجري 🏃‍♂️")
print("سيتم جمع أوقات الرياضات الثلاث وتحديد الفائز الأقل وقتًا.\n")

# دالة لإدخال بيانات لاعب
def get_player_data(player_num):
    print(f"\n🔻 اللاعب {player_num}")
    name = input("اكتب الاسم الثلاثي: ")
    swim = float(input("⏱️ وقت السباحة (بالدقائق): "))
    bike = float(input("⏱️ وقت ركوب الدراجة (بالدقائق): "))
    run = float(input("⏱️ وقت الجري (بالدقائق): "))
    total = swim + bike + run
    return {
        "name": name,
        "swim": swim,
        "bike": bike,
        "run": run,
        "total": total
    }

# إدخال بيانات اللاعبين
player1 = get_player_data(1)
player2 = get_player_data(2)

# عرض النتائج
print("\n📊 النتائج النهائية:")

def print_summary(player):
    print(f"\n📌 المتسابق: {player['name']}")
    print(f"  🏊 السباحة: {player['swim']} دقيقة")
    print(f"  🚴 ركوب الدراجة: {player['bike']} دقيقة")
    print(f"  🏃 الجري: {player['run']} دقيقة")
    print(f"  🧮 المجموع: {player['total']} دقيقة")

print_summary(player1)
print_summary(player2)

# تحديد الفائز
print("\n🥇 النتيجة:")
if player1["total"] < player2["total"]:
    print(f"🎉 الفائز هو: {player1['name']} بوقت {player1['total']} دقيقة!")
elif player2["total"] < player1["total"]:
    print(f"🎉 الفائز هو: {player2['name']} بوقت {player2['total']} دقيقة!")
else:
    print("🏁 تعادل! كلا المتسابقين لهما نفس الوقت.")

