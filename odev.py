ödev 5


#soru1
select * from film
where title like '%n'
order by length desc
limit 5

#soru 2
select * from film
where title like '%n'
order by length desc
(soruyu anlamadım)


#soru 3 
select * from customer
where store_id ='1'
order by last_name desc 

limit 4

odev 6

#soru1
select avg(rental_rate ) from film



#soru2
select count(title) from film
where title like '%'

#soru3
select LENGTH from film
where rental_rate ='0.99'
Order BY LENGTH DESC 
LIMIT 1


#SORU4

select COUNT(replacement_cost ) from film
where LENGTH > 150 




ödev 7

#soru1

select * from film

order by rating


#soru 2

select replacement_cost,count(*) from film

group by replacement_cost

having count(*)> 50

#soru 3

select store_id, count(*) from customer

group by store_id


#soru 4
select country_id , count(*) from city

group by country_id 

order by count(*) desc

limit 1




