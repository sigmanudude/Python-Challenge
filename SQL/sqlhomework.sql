use sakila;
#1a
select first_name, last_name 
from actor;

#1b
select concat(first_name, ' ' , last_name) as 'Actor Name'
from actor;

#2a
select actor_id, first_name, last_name
from actor
where first_name = 'Joe';

#2b
select last_name
from actor
where last_name like '%GEN%';

#2c
select last_name, first_name
from actor
where last_name like '%LI%';

#2d
SELECT country_id, country
FROM country
WHERE country IN
(
   SELECT country
   FROM country
   WHERE country = 'Afghanistan' or country = 'Bangladesh' or country = 'China'
  );

#3a
ALTER TABLE actor
ADD Description BLOB;

#3b
ALTER TABLE actor
DROP Description;

#4a
select last_name, count(last_name)
from actor
group by last_name;

#4b
select last_name, count(last_name)
from actor
group by last_name
having count(last_name) >=2;

#4c
update actor set first_name = 'HARPO', last_name = 'WILLIAMS'
where first_name = 'GROUCHO';

#4d
update actor set first_name = 'GROUCHO', last_name = 'WILLIAMS'
where first_name = 'HARPO';

#5a
select * from information_schema.tables;

#6a
SELECT staff.first_name, staff.last_name, address.address
FROM address
INNER JOIN staff ON
staff.staff_id = address.address_id;

#6b
SELECT staff.first_name, staff.last_name, payment.staff_id, payment.payment_date, sum(payment.amount) as 'Total Amount'
FROM staff
INNER JOIN payment ON
payment.staff_id = staff.staff_id 
where payment.payment_date >= '2005-08-01 00:00:00' and payment.payment_date < '2005-08-31 99:99:99'
GROUP BY staff.staff_id;

#6c
SELECT film_actor.film_id, film_actor.actor_id, film.film_id, film.title
FROM film
INNER JOIN film_actor ON
film_actor.film_id = film.film_id;

#6d
SELECT inventory.film_id, count(inventory.inventory_id) as 'Total Inventory', film.title
FROM film
INNER JOIN inventory ON
inventory.film_id = film.film_id
where film.title = 'Hunchback Impossible';

#6e
SELECT c.customer_id, c.last_name, sum(p.amount) as 'Total Paid'
FROM customer c
INNER JOIN payment p ON
c.customer_id = p.customer_id 
GROUP BY c.customer_id 
ORDER BY c.last_name;