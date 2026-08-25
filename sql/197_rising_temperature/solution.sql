select w.id
from weather as w join weather as sw
on w.recordDate - sw.recordDate = 1
where w.temperature > sw.temperature;
