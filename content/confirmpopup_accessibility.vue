<script setup>
const confirm = useConfirm();
const isVisible = ref(false);
const openPopup = (event) => {
    confirm.require({
        target: event.currentTarget,
        message: 'Are you sure you want to proceed?',
        header: 'Confirmation',
        onShow: () => {
            isVisible.value = true;
        },
        onHide: () => {
            isVisible.value = false;
        }
    });
}
</script>