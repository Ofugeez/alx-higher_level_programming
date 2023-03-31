def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""

    if not list_of_integers:
        return None
    
    lo, hi = 0, len(list_of_integers) - 1
    
    while lo < hi:
        mid = (lo + hi) // 2
        mid_right = list_of_integers[min(mid + 1, hi)]
        mid_left = list_of_integers[max(mid - 1, lo)]
        
        if list_of_integers[mid] >= mid_right and list_of_integers[mid] >= mid_left:
            return list_of_integers[mid]
        elif mid_right > list_of_integers[mid]:
            lo = mid + 1
        elif mid_left > list_of_integers[mid]:
            hi = mid - 1
            
    return list_of_integers[lo]