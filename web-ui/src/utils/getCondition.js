function getCondition(protocolsList) {
    let condition = '('
    const ids = protocolsList.map((protocol) => {
      return protocol.id
    })

    ids.forEach(elem => {
      if (elem === ids[ids.length - 1]) {
        condition += `${elem})`
      }
      else {
        condition += `${elem},`
      }
    });
    return condition
  }

export default getCondition

