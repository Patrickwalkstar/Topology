###This is a tutorial on how to determine a polynomial precursor parametrization for a knot diagram:
1. Assign unique identities to each intersection
2. Determine whether each intersection has a positive orientation or negative orientation
3. Determine a direction to follow along the length of the knot.
4. For each complete strand you come to along the length of the knot perform the following:
    - record the intersection the strand starts at. if it is a positive orientation record a 1 with the identity of the intersection.
    - if it is a negative orientaiton, record a -1.
        - record the intersection and the directionality number (+1 or -1 as stated previously) as a parametrization
    - record each intersection the strand passes through (overcrossing). the strand has a directionality of 0 for these intersecions
        - record the intersections and their directionality number (in this case 0) as pairs
    - record the intersection the strand terminates at. if it is a positive orientation record a -1 for the directionality number, and
    - if it is a negative orientation, record a 1.
        - record the intersection and the directionality number as a pair
    - the notation for each strand is the collection of pairs generated in this manner with the intersections in order along the length of strand
5. The notation for the knot diagram is the list of strands

***Overall**, the polynomial precursor parametrization for a knot diagram will look like a list of strands which are lists of pairs of an intersection and a directionality number*