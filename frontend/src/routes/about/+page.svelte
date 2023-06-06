<script>
  import { Heading, P, A, Span } from "flowbite-svelte";
  import {
    Navbar,
    NavBrand,
    NavLi,
    NavUl,
    NavHamburger,
  } from "flowbite-svelte";
  import { page } from "$app/stores";
  import { onMount } from "svelte";
</script>

<Navbar let:hidden let:toggle>
  <NavBrand href="/">
    <img src="/Frame.svg" class="self-center w-4/6 py-3" alt="Logo" />
  </NavBrand>
  <NavHamburger on:click={toggle} />
  <NavUl {hidden}>
    <NavLi
      href="/"
      active={$page.url.pathname === "/" ? true : false}
      class="flex items-center text-xl"
    >
      <img src="/EMMA.svg" class="w-9 h-10 px-3" alt="Logo" />LOGIN</NavLi
    >

    <NavLi
      href="/about"
      active={$page.url.pathname === "/about" ? true : false}
      class="flex items-center  text-xl"
    >
      <img src="/EMMA.svg" class="w-9 h-10 px-3" alt="Logo" />ABOUT</NavLi
    >
  </NavUl>
</Navbar>

<Heading tag="h2" class="mt-5 mb-2">About</Heading>
<Heading tag="h5" class="font-light"
  >EMMA는 대학생들을 위한 포트폴리오 정리 웹사이트입니다.</Heading
><P class="mb-3">
  이 웹사이트는 학생들이 자신의 관심 직무, 자격 사항, 전공, 그리고 공모전 및
  비교과 활동을 효과적으로 관리하고 소개할 수 있도록 도와줍니다.</P
>
<Heading tag="h4" class="mt-10 mb-2">EMMA란?</Heading>
<P class="m-3 flex items-center">
  <img src="/EMMA.svg" class="w-10 h-10 m-3 mr-6" alt="Logo" />
  <Heading tag="h3" class="w-fit p-3"
    ><Span gradient size="xl">EMMA</Span></Heading
  >는 보라색 눈꽃 모양의 로고를 가지고 있으며, 눈이 쌓이듯이 학생들의 실력과
  실적이 쌓여나가는 모습을 상징합니다. 또한, EMMA라는 이름은 "who am I"를 빠르게
  발음하면 나오는 단어로, 학생들이 자신을 나타내고 자신의 역량을 활용하여
  성장하고 발전하기를 바라는 의미가 담겨 있습니다.
</P>

<Heading tag="h4" class="mt-10 mb-2">EMMA Web</Heading>
<P class="mb-3">
  <img src="/Screenshot.jpg" alt="Logo" />EMMA 웹사이트는 사용자 친화적인
  인터페이스와 간편한 기능을 제공하여 학생들이 자신의 포트폴리오를 관리하는
  과정을 용이하게 만듭니다. 관심 직무를 선택하고 해당 직무에 필요한 자격 사항을
  등록하면, EMMA는 사용자에게 필요한 스킬과 경험을 제안하고 관련된 자료와
  리소스를 제공합니다. 학생들은 자신의 전공을 등록하고 관련된 과목, 연구,
  프로젝트 등을 기록하며, 공모전 및 비교과 활동에 대한 정보를 추가할 수
  있습니다. EMMA는 사용자들이 손쉽게 포트폴리오를 구성하고 관리할 수 있도록
  다양한 템플릿과 커스터마이징 옵션을 제공합니다. EMMA는 대학생들에게 자신의
  역량을 명확하게 보여줄 수 있는 플랫폼으로, 취업 준비나 대학진학에 도움이 되는
  강력한 도구입니다. 사용자들은 EMMA를 통해 자신의 성과와 능력을 시각적으로
  표현하고, 관심 있는 기업이나 대학에 소개할 수 있습니다. EMMA는 학생들이 자신의
  미래에 대한 비전을 구체화하고, 발전과 성공을 위한 첫걸음을 내딛을 수 있도록
  돕는 믿을 수 있는 동반자입니다.</P
>
