select s.student_id, s.student_name, s.subject_name, coalesce(a.count, 0) as attended_exams
from
    (select student_id, student_name, subject_name
    from students cross join subjects
    order by (student_id, subject_name)) as s
left join
    (select student_id, subject_name, count(*)
    from examinations
    group by (student_id, subject_name)) as a
on s.student_id = a.student_id and s.subject_name = a.subject_name
