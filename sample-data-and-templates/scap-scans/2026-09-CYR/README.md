# CYR Fictitious ATO Scan Dataset

These are renamed copies of existing scans for a fictitious OpenRMF Professional
ATO demonstration. They are not new assessments of actual CYR machines.

## Files and identity mapping

* This directory contains 94 SCAP XML results copied from
  [the September 2026 scans](../2026-09/).
* [The matching patch dataset](../../patch-vulnerability-scans/2026-CYR/)
  contains seven Nessus scans copied from the files beginning with `2026` in
  [the original patch scan directory](../../patch-vulnerability-scans/).
  Their date-based filenames are unchanged.
* [host-mapping.csv](./host-mapping.csv) lists all 11 Windows hosts and the SQL
  instance alias. Servers use `CYR-` instead of `SOT-`; workstations use
  `CYR-WKS1` through `CYR-WKS7`. Each mapped IPv4 address becomes
  `10.10.20.<original last octet>`.
* `CYR-WIN2K22-SQL-SQLEXPRESS` is the SQL instance target on
  `CYR-WIN2K22-SQL`, sharing `10.10.20.168`. It is not a twelfth host.

Mapped hostnames and addresses are replaced throughout both scan formats,
including embedded evidence, identity facts, FQDN host portions, scan target
lists, and host-qualified account references. SCAP filenames are also renamed.
The original scan files are unchanged.

## Preserved data and limitations

Scan dates, findings, results, scores, benchmark/rule/plugin identifiers,
severities, and remediation guidance are preserved. XML formatting, namespaces,
and line endings are preserved as well.

The `TUTLAN` DNS suffix, MAC addresses (including historical variants), usernames,
and unrelated metadata remain unchanged. Other network references, such as
gateway/DNS addresses, are not remapped unless they are one of the mapped host
addresses. These files are a renamed demonstration dataset, **not fully
anonymized data** or a complete representation of a newly configured network.

## Suggested OpenRMF Professional import

1. Create a separate fictitious system package for the CYR ATO; do not combine
   these scans with the original SOT assets.
2. Upload the XML files in this directory using the SCAP scan import workflow.
3. Upload the Nessus files from the matching patch directory using the patch
   vulnerability import workflow. Use their embedded dates when reviewing
   historical changes.
4. Verify that SCAP and patch results correlate to the same 11 CYR hosts and
   mapped IP addresses. Check the SQL instance against its parent server.
   Because original MAC addresses are retained, confirm that imports do not
   correlate with original assets in your OpenRMF deployment.

Local validation parsed all 101 generated XML documents, checked host/IP
consistency across both formats, and confirmed preservation of 6,575 SCAP rule
results and 13,392 Nessus vulnerability report items. All duplicate bytes match
the source with only the mapped identity substitutions, and source checksums
are unchanged. Actual OpenRMF Professional ingestion and correlation must still
be verified in your deployment.
