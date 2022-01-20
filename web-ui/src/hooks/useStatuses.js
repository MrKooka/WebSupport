import { useMemo } from "react";

export const useSortedStatusrs = (statuses, sort) => {
    const sortedStatuses= useMemo(() => {
        if (sort) {
            return [...statuses].sort((a, b) => {
                console.log(a[sort])
                // a[sort].localeCompare(b[sort])
            })
        }
        return statuses
    },
        [sort, statuses])
    return sortedStatuses
}

export const useStatuses= (statuses, sort, query) => {
    console.log(sort);
    // const sortedStatuses = useSortedStatusrs(statuses, sort)
    const sortedStatuses = useMemo(() => {
        return statuses.filter(status => status.type.toLowerCase().includes(sort.toLowerCase()))
    }, [query, statuses])
    return sortedStatuses
}