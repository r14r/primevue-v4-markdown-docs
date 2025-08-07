<Drawer v-model:visible="visible">
    <template #header>
        <div class="flex items-center gap-2">
            <Avatar image="/images/avatar/amyelsner.png" shape="circle" />
            <span class="font-bold">Amy Elsner</span>
        </div>
    </template>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
    <template #footer>
        <div class="flex items-center gap-2">
            <Button label="Account" icon="pi pi-user" class="flex-auto" variant="outlined"></Button>
            <Button label="Logout" icon="pi pi-sign-out" class="flex-auto" severity="danger" text></Button>
        </div>
    </template>
</Drawer>
<Button icon="pi pi-plus" @click="visible = true" />