import data from '../../../shared/overview-page-data.json'
import { randomMessage } from '../utils'

type QueryCase = {
    query: string,
    len: number
}

const queryLengths = [0, 2, 39, 40, 41]

export const queries = queryLengths.map(queryCase)

function queryCase(len: number): QueryCase {
    return {
        query: randomMessage(len),
        len: len
    }
}

export const categoryNames = data.categoryNames