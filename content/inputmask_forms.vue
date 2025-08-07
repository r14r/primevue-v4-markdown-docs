<Form v-slot="$form" :resolver="resolver" :initialValues="initialValues" @submit="onFormSubmit" class="flex flex-col gap-4 w-full sm:w-56">
    <div class="flex flex-col gap-1">
        <InputMask name="serialNumber" mask="99-999999" placeholder="99-999999" fluid />
        <Message v-if="$form.serialNumber?.invalid" severity="error" size="small" variant="simple">{{ $form.serialNumber.error?.message }}</Message>
    </div>
    <Button type="submit" severity="secondary" label="Submit" />
</Form>