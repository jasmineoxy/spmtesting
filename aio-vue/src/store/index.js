import { createStore } from 'vuex';


const store = createStore({
  state() {
    return {
      user: 'learner',
      employeeId: '3',
      employeeName: 'John Doe'
    };
  },
  mutations: {
    changeUser(state, payload) {
      state.user = payload;
    }
  },
  actions: {
      setUser(context, payload){
          context.commit('changeUser', payload)
      }
  },
  getters: {
      getUserState(state){
          return state.user;
      },
      getUserDetails(state){
        var result = {
          'employeeId': state.employeeId,
          'employeeName': state.employeeName
        }
        return result;
      }
  }
});

export default store;