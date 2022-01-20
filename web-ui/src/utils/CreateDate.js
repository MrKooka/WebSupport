export const CreateDate = (props, offerEndDateTime = false, updateForm = null) => {
    const tzoffset = (new Date()).getTimezoneOffset() * 60000; //offset in milliseconds

    if (offerEndDateTime && updateForm.procedure.offerDate) {
        let oldDate = Date.parse(updateForm.procedure.offerDate) - tzoffset
        const newDate = new Date(oldDate + 10800000).toISOString().slice(0, 19).replace('T', ' ').replace('Z', '')
        return newDate
    }
    if (props.value) {

        let oldDate = Date.parse(props.value) - tzoffset
        const newDate = new Date(oldDate).toISOString().slice(0, 19).replace('T', ' ').replace('Z', '')
        return newDate
    }
}
