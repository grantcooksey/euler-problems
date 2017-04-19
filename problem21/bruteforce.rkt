#lang racket

;; Create a list of all divisors of the starting number.  x and curr should be
;; the same when starting.  
(define (get-divisors x curr)
  (cond
    [(equal? curr 0) `()]
    [(and (equal? (modulo x curr) 0) (not (equal? curr x)))
     (cons curr (get-divisors x (- curr 1)))]
    [else (get-divisors x (- curr 1))]))

;;(get-divisors 220 220)
;;(get-divisors 284 284)