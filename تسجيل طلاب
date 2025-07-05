# استدعاء من مكتبة بايثون
import tkinter as tk

# كتابة خصائص النافذه
wendo = tk.Tk()
wendo.title("تسجيل الطلاب")
wendo.geometry("400x300")

# القائمة
students  = []

#الدوال
#دالة زر التسجيل
def registration():
    name = entry.get()
    if name == "":
        result_label.config(text="❌ لا يمكن ترك الخانة فارغة")
    elif name in students:
        result_label.config(text="❌ لا يمكن الاسم موجود بالفعل")
    else:
        students.append(name)
        result_label.config(text=f"تم تسجيل {name} ✅")
        entry.delete(0 , tk.END)

#دالة العرض
def the_offer ():
    if not students:
        result_label.config(text="📭 لا يوجد طلاب مسجلين حتى الآن")
    else:
        all_names = "\n".join(students)
        result_label.config(text=f"📋 قائمة الطلاب:\n{all_names}")

# استدعاء الزر و النص و الخانه
#Label = النص
label = tk.Label(wendo ,  text="ادخل اسم الطالب:")
label.pack(pady=5)


#Entry = الكتابة
entry = tk.Entry(wendo)
entry.pack(pady=5)

#Button = الزر
button = tk.Button(wendo , text="تسجيل" , command=registration)
button.pack(pady=5)
#زر المسجلين
button= tk.Button(wendo , text="عرض الاسماء الطلاب المسجلين", command=the_offer)
button.pack(pady=5)

# الدالة والاستدعاء
result_label = tk.Label(wendo, text="")
result_label.pack(pady=5)


wendo.mainloop()
