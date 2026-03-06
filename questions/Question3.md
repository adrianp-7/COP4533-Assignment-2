# Question 3: Prove OPTFF is Optimal

**Claim:** For any request sequence and cache size k, OPTFF never incurs more misses than any offline algorithm A.

## Proof by Induction on sequence length m

**Base case (m = 1):** Any algorithm misses at most once. OPTFF does the same.

**Inductive hypothesis:** OPTFF is optimal for all sequences of length less than m.

**Inductive step:** Take a sequence of length m and consider the first request r₁.

If r₁ is already cached, nobody misses and both algorithms face the same remaining m−1 requests — optimal by hypothesis.

If r₁ is a miss and the cache has room, both load r₁ with no eviction and again reduce to the m−1 case.

The interesting case is when r₁ is a miss and the cache is full. Both algorithms must evict something. Say A evicts item g and OPTFF evicts item f, where f is used farthest in the future, so next(f) ≥ next(g). If we force A to evict f instead of g, nothing gets worse — g isn't requested before f anyway, so the cache contents are just as useful until next(f). From that point the two algorithms face an identical situation, and OPTFF is optimal on what remains by the inductive hypothesis.

In every case misses(OPTFF) ≤ misses(A), which completes the induction. ∎