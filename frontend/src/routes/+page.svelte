<script>
  import {
    Button,
    Modal,
    Label,
    Input,
    Checkbox,
    Heading,
  } from "flowbite-svelte";

  let id;

  async function fetch_result() {
    try {
      const response = await fetch(
        `http://10.125.218.100:9025/result?id=${id}`,
        {
          mode: "cors",
        }
      );

      if (response.ok) {
        const result = await response.json();
        console.log(result);
        document.location.href = `/emma/${id}`;
      } else {
        console.error("Error:", response.status);
      }
    } catch (error) {
      console.error("Error:", error);
    }
  }
</script>

<div class="h-full w-full p-52">
  <form class="flex flex-col space-y-6" action="#">
    <Heading tag="h2" class="mt-5 mb-2">Login</Heading>
    <Label class="space-y-2">
      <span>EMMA ID</span>
      <Input
        bind:value={id}
        type="text"
        name="EMMA ID"
        placeholder="Your EMMA ID"
        required
      />
    </Label>
    <Label class="space-y-2">
      <span>password</span>
      <Input
        type="password"
        name="current-password"
        placeholder="•••••••••••••••"
        required
      />
    </Label>

    <Button on:click={() => fetch_result()} class="w-full"
      >Login to your account</Button
    >
    <div class="text-sm font-medium text-gray-500 dark:text-gray-300">
      Not registered? <a
        href="/register"
        class="text-blue-700 hover:underline dark:text-blue-500"
        >Create account</a
      >
    </div>
  </form>
</div>
