<template>
    <tr>
        <td>
            {{id}}
        </td>
        <td>
            {{ startDate}}
        </td>
        <td>
            {{ endDate }}
        </td>
        <td>
            {{ classStartTime }}
        </td>
        <td>
            {{ classEndTime }}
        </td>
        <td>
            {{ classDay }}
        </td>
        <td>
            {{ currentClassSize }}
        </td>
        <td>
            {{ maxClassSize }}
        </td>
        <td>
            {{ trainerName }}
        </td>
        <td>
            <base-button @click="requestEnrollment">{{enrollStatusMessage}}</base-button>
        </td>
    </tr>
</template>
<script>
export default {
    props: ['id','startDate','endDate', 'classStartTime', 'classEndTime', 'classDay', 'currentClassSize', 'maxClassSize', 'trainerName'],
    data() {
        return {
            enrollStatusMessage: 'Enroll Class',
            wantsToEnroll: false,
        }
    },
    methods: {
        requestEnrollment() {
            this.wantsToEnroll = ! this.wantsToEnroll
            if (this.wantsToEnroll){
                return this.enrollStatusMessage = "Enrollment Requested"
            }
            return this.enrollStatusMessage = "Enroll Class"
        }
    }
}
</script>