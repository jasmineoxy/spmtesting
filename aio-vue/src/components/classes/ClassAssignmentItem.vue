<template>
    <tr>
        <td>
            {{eachLearnerId[0]}}
        </td>
        <td>
            {{ eachLearnerId[1]}}
        </td>
        <td>
            Yes
        </td>
        <td>
            <base-button @click="assignLearner">{{assignLearnerStatus}}</base-button>
        </td>
    </tr>
</template>
<script>
export default {
    props: ['eachLearnerId'],
    data() {
        return {
            assignLearnerStatus: 'Assign',
            wantToAssign: false,
        }
    },
    methods: {
        assignLearner() {
            this.wantToAssign = ! this.wantToAssign
            if (this.wantToAssign){
                return this.assignLearnerStatus = "Assigned"
            }
            return this.assignLearnerStatus = "Assign"
            }
    }
}
</script>