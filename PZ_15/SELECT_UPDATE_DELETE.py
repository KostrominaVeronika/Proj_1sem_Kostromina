import sqlite3
with sqlite3.connect('decanat.db') as con:
    cur = con.cursor()
    # Вывести список всех студентов, зачисленных на факультет, с указанием номера
    # группы.
    cur.execute("""
    SELECT spec.name AS name_spec, fac.name AS name_fac, card_student.FIO_s, card_student.group_st FROM spec
    JOIN dep ON spec.dep_id = dep.id_dep
    JOIN fac ON dep.fac_id = fac.id_fac
    JOIN card_student ON spec.id_spec = card_student.id_spec;
    """)
    # Вывести список всех студентов и кафедр, на которых они обучаются
    cur.execute("""
    SELECT card_student.FIO_s AS fio_stud, dep.name AS name_dep FROM spec
    JOIN card_student ON spec.id_spec = card_student.id_spec
    JOIN dep ON spec.dep_id = dep.id_dep;
    """)
    # Вывести список всех предметов и количество лекционных часов, выделенных на каждый
    # предмет в учебном плане каждой специальности.
    cur.execute("""
    SELECT items.name, plan.amount_lec FROM items
    JOIN plan ON items.id_item = plan.id_item;
    """)
    # Вывести список всех студентов, у которых есть неудовлетворительные оценки
    # (меньше 4) по любому предмету.
    cur.execute("""
    SELECT FIO_s FROM card_student WHERE rating<4;
    """)
    # Вывести список всех предметов, которые изучают студенты.
    cur.execute("""
    SELECT items.name FROM card_student
    JOIN items ON card_student.id_item = items.id_item;
    """)
    # Вывести список всех студентов, которые сдают курсовую работу.
    cur.execute("""
    SELECT card_student.FIO_s FROM card_student 
    JOIN form ON card_student.id_form = form.id_form
    WHERE form.name="Курсовая работа";
    """)
    # Вывести список всех предметов, которые изучают студенты группы 23.
    cur.execute("""
    SELECT items.name FROM card_student
    JOIN items ON card_student.id_item = items.id_item
    WHERE card_student.group_st = "23";
    """)
    # Вывести список всех абитуриентов, зачисленных на специальность "Информатика
    # и вычислительная техника".
    cur.execute("""
    SELECT card_student.FIO_s, card_student.rating FROM card_student
    JOIN spec ON card_student.id_spec = spec.id_spec
    WHERE spec.name = "ИС";
    """)
    # Вывести список студентов и их оценки за все предметы на специальности
    # "математика"
    cur.execute("""
    SELECT FIO_s, rating
    FROM card_student
    JOIN items ON card_student.id_item = items.id_item
    WHERE items.name = "математика"
    """)

    # SQL-запросы на обновление
    # Обновление названия факультета с id=1 на "Новый факультет"
    cur.execute("""
    UPDATE fac SET name="Новый факультет" WHERE id_fac="1";
    """)
    # Обновление названия кафедры с id=2 на "Новая кафедра"
    cur.execute("""
    UPDATE dep SET name="Новая кафедра" WHERE id_dep="2";
    """)
    # Обновление названия специальности с id=3 на "Новая специальность"
    cur.execute("""
    UPDATE spec SET name="Новая специльаность" WHERE id_spec="3";
    """)
    # Обновление названия предмета с id=4 на "Новый предмет"
    cur.execute("""
    UPDATE items SET name="Новый предмет" WHERE id_item="4";
    """)
    # Обновление названия формы сдачи предмета с id=5 на "Новая форма сдачи"
    cur.execute("""
    UPDATE form SET name="Новый форма сдачи" WHERE id_form="5";
    """)
    # Обновление количества лекционных часов на 30 для учебного плана с id=6
    cur.execute("""
    UPDATE plan SET amount_lec = 30 WHERE id_plan="6";
    """)
    # Обновление количества лекционных часов у предмета "математика" на учебном
    # плане специальности "ИБТ"
    cur.execute("""
    UPDATE plan
    SET amount_lec = 142
    WHERE id_item IN (SELECT id_item FROM items WHERE name = "математика")
    AND id_spec IN (SELECT id_spec FROM spec WHERE name = "ИБТ");
    """)
    # Обновление количества лабораторных часов и формы сдачи предмета у
    # специальности "ИКС" для предмета "кибернетика"
    cur.execute("""
    UPDATE plan
    SET amount_lab = 144, id_form = 5
    WHERE id_item IN (SELECT id_item FROM items WHERE name = "кибернетика")
    AND id_spec IN (SELECT id_spec FROM spec WHERE name = "ИКС");
    """)
    # Обновление количества лекционных и практических часов у предмета
    # "менеджмент" на учебном плане кафедры "ЧВК"
    cur.execute("""
    UPDATE plan
    SET amount_lec = 46, amount_prac = 89
    WHERE id_item IN (SELECT id_item FROM items WHERE name = "менеджмент")
    AND id_spec IN (SELECT id_spec FROM spec WHERE name = "ЧВК");
    """)
    # Обновить кол-во лекционных часов для всех предметов, где количество
    # лекционных часов больше 30
    cur.execute("""
    UPDATE plan
    SET amount_lec = 500
    WHERE amount_lec > 30;
    """)
    # Обновить фамилию и имя абитуриента по его идентификатору
    cur.execute("""
    UPDATE abitur
    SET name="МИХАИЛ", last_name="ШОЛОХОВ"
    WHERE id_abit=3;
    """)
    # Обновить название кафедры для всех специальностей, где кафедра имеет id = 1
    cur.execute("""
    UPDATE dep
    SET name="НОВАЯ КАФЕДРА С ID=1"
    WHERE id_dep=1;
    """)
    # Обновить оценку по определенному предмету и форме сдачи для конкретного
    # студента
    cur.execute("""
    UPDATE card_student
    SET rating=3
    WHERE id_item IN (SELECT id_item FROM items WHERE name = "химия")
    AND id_form IN (SELECT id_form FROM form WHERE name = "Новый форма сдачи")
	AND FIO_s = "Рык Архип Геннадьевич";
    """)
    # Обновить название специальности для всех студентов, где специальность имеет id = 1
    cur.execute("""
    UPDATE spec
    SET name="НОВАЯ СПЕЦ С ID=1"
    WHERE id_spec=1;
    """)
    # Обновить все оценки студента с фамилиец "Рык" на предмете "химия" на
    # значение 4
    cur.execute("""
    UPDATE card_student
    SET rating=4
    WHERE substr(FIO_s, 1, instr(FIO_s, ' ') - 1) = "Рык"
    AND id_item IN (SELECT id_item FROM items WHERE name = "химия")
    """)
    # Обновить название факультета на "Факультет информационных технологий" для
    # всех кафедр, относящихся к этому факультету
    cur.execute("""
    UPDATE fac
    SET name = "Факультет информационных технологий"
    WHERE name = "компьютерных наук"
    """)
    # Обновить количество лабораторных часов на предмете "Физика" для
    # специальности "Физика и информатика" на 30
    cur.execute("""
    UPDATE plan
    SET amount_lab = 30
    WHERE id_item IN (SELECT id_item FROM items WHERE name = "философия")
    AND id_spec IN (SELECT id_spec FROM spec WHERE name = "ППП");
    """)
# Удалить всех студентов, которые учатся на специальности "Информационные технологии" и сдали экзамен по предмету "Алгоритмы и структуры данных" на более низкую оценку, вместе с их учебными карточками
# Удалить всех студентов, которые не сдали экзамен по предмету "Физика" в установленный срок, вместе с их учебными карточками
    # SQL-запросы на удаление данных
    # Удалить всех абитуриентов, у которых дата поступления ранее 2020 года
    cur.execute("""
    DELETE FROM abitur 
    WHERE date_b < '2020-01-01'
    """)
    # Удалить все учебные планы, которые не связаны ни с одной специальностью.
    cur.execute("""
    DELETE FROM plan 
    WHERE plan.id_spec NOT IN (SELECT id_spec FROM spec)
    """)
    # Удалить все кафедры, которые не относятся ни к одному факультету
    cur.execute("""
    DELETE FROM dep 
    WHERE dep.fac_id NOT IN (SELECT id_fac FROM fac )
    """)
    # Удалить все предметы, которые не входят ни в один учебный план.
    cur.execute("""
    DELETE FROM items 
    WHERE id_item NOT IN (SELECT id_item FROM plan)
    """)
    # Удалить всех студентов, не имеющих оценок.(у нас у всех студентов есть оценки)
    cur.execute("""
    DELETE FROM card_student 
    WHERE rating IS NULL
    """)
    # Удалить все записи из таблицы "Учебная карточка" для предмета "Математика" с формой сдачи "Экзамен"
    cur.execute("""
    DELETE FROM card_student 
    WHERE id_item IN (SELECT id_item FROM items WHERE name = "математика")
    AND id_form IN (SELECT id_form FROM form WHERE name = "Экзамен")
    """)
    # Удалить все записи из таблицы "Учебная карточка" для студентов, обучающихся на факультете "Новый факультет"
    cur.execute("""
    DELETE FROM card_student 
    WHERE id_spec IN (SELECT id_spec FROM spec WHERE dep_id IN (SELECT id_dep FROM dep WHERE fac_id IN (SELECT id_fac FROM fac WHERE name="Новый факультет")))
    """)
    # Удалить все записи из таблицы "Учебная карточка" для студентов, не сдавших ни одного экзамена (нет такого атрибута в таблице)
    cur.execute("""
    DELETE FROM card_student 
    WHERE rating IS NULL
    """)
    # Удалить всех абитуриентов, которые не поступили на заданную специальность
    cur.execute("""
    DELETE FROM abitur 
    WHERE id_spec NOT IN (SELECT id_spec FROM spec WHERE name="ИКС")
    """)
    # Удалить все учебные карточки, связанные с предметом, который больше не входит в учебный план по заданной специальности
    cur.execute("""
    DELETE FROM card_student 
    WHERE id_item NOT IN (SELECT id_item FROM plan WHERE id_spec IN (SELECT id_spec FROM spec WHERE name="СА"))
    """)
    # Удалить все учебные карточки, связанные с заданной формой сдачи предмета
    cur.execute("""
    DELETE FROM card_student
    WHERE id_form IN (SELECT id_form FROM form WHERE name="Зачет")
    """)
    # Удалить всех абитуриентов, не зачисленных на заданную специальность
    cur.execute("""
    DELETE FROM abitur 
    WHERE id_spec NOT IN (SELECT id_spec FROM spec WHERE name="ИКС")
    """)
    # Удалить всех абитуриентов, которые подавали заявку на специальность с названием "НОВАЯ СПЕЦ С ID=1"
    cur.execute("""
    DELETE FROM abitur 
    WHERE id_spec IN (SELECT id_spec FROM spec WHERE name="НОВАЯ СПЕЦ С ID=1");
    """)
    # Удалить всех студентов, которые учатся на специальности "ИБА"
    # и сдали экзамен по предмету "математика" на
    # более низкую оценку
    cur.execute("""
    DELETE FROM card_student
    WHERE id_spec IN (SELECT id_spec FROM spec WHERE name="ИБА")
    AND id_item IN (SELECT id_item FROM items WHERE name="математика")
    AND rating < 3
    """)
    con.commit()
