import {
    createStore
} from 'vuex';

const store = createStore({
    state: {
        isCollapsed: false // 菜单是否折叠，默认展开
    },
    mutations: {
        toggleMenu(state) {
            state.isCollapsed = !state.isCollapsed; // 切换菜单折叠状态
        }
    }
});

export default store;