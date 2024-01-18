-- SQL script that ranks country origins of bands
Select
    origin,
    sum(fans) as nb_fans
from
    metal_bands
group by
    origin
order by
    nb_fans desc;