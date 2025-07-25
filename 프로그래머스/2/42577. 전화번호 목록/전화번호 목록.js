function solution(phone_book) {
    const hash_map = {};
    
    for (const phone of phone_book) {
        hash_map[phone] = 1;
    }
    
    for (const phone of phone_book) {
        let prefix = "";
        for (let i = 0; i < phone.length - 1; i++) {
            prefix += phone[i];
            if (hash_map[prefix]) {
                return false;
            }
        }
    }
    
    return true;
}