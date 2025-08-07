<script setup>
/* ProductListDemo.vue */
const emit = defineEmits(['cancel', 'save'])

function buttonClick() {
    emit('cancel', {user: 'primetime'});
}

function saveButtonClick() {
    emit('save', {user: 'primetime'});
}
</script>