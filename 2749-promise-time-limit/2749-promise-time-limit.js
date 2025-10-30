/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
    return async function(...args) {
        return Promise.race([
            fn(...args), // actual function
            new Promise((_, reject) => 
                setTimeout(() => reject("Time Limit Exceeded"), t)
            )
        ]);
    };
};
