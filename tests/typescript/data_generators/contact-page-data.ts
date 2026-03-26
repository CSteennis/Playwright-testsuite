import { ContactFormData } from '../pages/contact-page'
import data from '../../../shared/contact-page-data.json'
import { randomMessage } from '../utils'

export const subjectOptions = data.expectedOptions as readonly string[]

export const formData = data.formDummyData as ContactFormData

export const formSuccessText = data.formSuccessText as string

export type MessageCase = {
    name: string
    message: string
    expectedError: string
}

const messageLengths = [0, 1, 49, 50, 51] as const

export const messageCases: MessageCase[] = messageLengths.map(createMessageTestCase)

function getErrorMessage(len: number): string {
    if (len === 0) return data.zeroCharError
    if (len > 0 && len < 50) return data.minCharError
    if (len >= 50) return ''
    throw new Error('Invalid message length')
}

function createMessageTestCase(len: number): MessageCase {
    return {
        name: `${len} chars`,
        message: randomMessage(len),
        expectedError: getErrorMessage(len),
    }
}

