#lang racket

(require rackunit)
(require srfi/1)

;; Create a list of all divisors of the starting number.  x and curr should be
;; the same when starting.  
(define (gen-divisors x curr)
  (cond
    [(equal? curr 0) `()]
    [(and (equal? (modulo x curr) 0) (not (equal? curr x)))
     (cons curr (gen-divisors x (- curr 1)))]
    [else (gen-divisors x (- curr 1))]))

;; wrapper
(define (get-divisors x)
  (gen-divisors x x))

(check-equal? (get-divisors 2) `(1))
(check-equal? (get-divisors 284) `(142 71 4 2 1))
(check-equal? (get-divisors 220) `(110 55 44 22 20 11 10 5 4 2 1))


;; Create a list of all the divisors and their sums. starts at 1
(define (build-divisor-sum range)
  (reverse
   (let bds ([r range])
    (cond
      [(<= r 0) `()]
      [else (cons (reduce + 0 (get-divisors r))
                  (bds (- r 1)))]))))

;;(build-divisor-sum 10)

;; given an number, determines if it has an amicable pair. Ignores number greater
;; than length of loi
(define (is-amicable n loi)
  (and (>= (length loi) (num-at n loi))
       (equal? n (num-at (num-at n loi) loi))
       (not (equal? (num-at n loi) n))))

;;helper for indexing since indexing starts at 1
(define (num-at n loi)
  (list-ref loi (- n 1)))

(check-equal? (is-amicable 2 `(5 3 2)) #t)
(check-equal? (is-amicable 2 `(5 2 2)) #f)
(check-equal? (is-amicable 2 `(54 3 4)) #f)
(check-equal? (is-amicable 2 `(2 100 2)) #f)
(check-equal? (is-amicable 220 (build-divisor-sum 1000)) #t)

;; given an upper bound, sum all amicable numbers lower than the bound
(define (sum-amicable n)
  (let ([div-sum (build-divisor-sum n)])
    (foldl + 0
           (let sa ([curr (- n 1)])
             (cond
               [(<= curr 1) `()]
               [(is-amicable curr div-sum) (cons (num-at curr div-sum)
                                                 (sa (- curr 1)))]
               [else (cons 0 (sa (- curr 1)))])))))

(sum-amicable 10000)
