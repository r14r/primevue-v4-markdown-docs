<ConfirmPopup group="headless">
    <template #container="{ message, acceptCallback, rejectCallback }">
        <div class="rounded p-4">
            <span>{{ message.message }}</span>
            <div class="flex items-center gap-2 mt-4">
                <Button label="Save" @click="acceptCallback" size="small"></Button>
                <Button label="Cancel" variant="outlined" @click="rejectCallback" severity="secondary" size="small" text></Button>
            </div>
        </div>
    </template>
</ConfirmPopup>
<Button @click="requireConfirmation($event)" label="Save"></Button>