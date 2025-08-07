<Form v-slot="$form" :resolver="resolver" :initialValues="initialValues" @submit="onFormSubmit" class="flex flex-col gap-4">
    <div class="flex flex-col gap-1">
        <Textarea name="address" rows="5" cols="30" style="resize: none" />
        <Message v-if="$form.address?.invalid" severity="error" size="small" variant="simple">{{ $form.address.error?.message }}</Message>
    </div>
    <Button type="submit" severity="secondary" label="Submit" />
</Form>